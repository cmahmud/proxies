# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 419
- HTTP: 100 alive / 77 gold
- HTTPS: 115 alive / 16 gold
- SOCKS4: 181 alive / 158 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42115
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
