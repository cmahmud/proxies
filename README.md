# SyndProxy validated proxy pool

## Current pool

- Alive now: 393
- Gold now: 320
- HTTP: 88 alive / 66 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 119 alive / 104 gold
- SOCKS5: 144 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49522
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
