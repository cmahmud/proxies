# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 444
- HTTP: 128 alive / 81 gold
- HTTPS: 124 alive / 34 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44724
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
