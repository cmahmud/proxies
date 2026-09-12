# SyndProxy validated proxy pool

## Current pool

- Alive now: 398
- Gold now: 328
- HTTP: 79 alive / 64 gold
- HTTPS: 40 alive / 24 gold
- SOCKS4: 125 alive / 107 gold
- SOCKS5: 154 alive / 133 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49497
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
