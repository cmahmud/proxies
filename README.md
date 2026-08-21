# SyndProxy private pool

## Current pool

- Alive now: 763
- Gold now: 402
- HTTP: 197 alive / 88 gold
- HTTPS: 130 alive / 22 gold
- SOCKS4: 206 alive / 146 gold
- SOCKS5: 230 alive / 146 gold

## Historical pool

- Discovered: 154725
- Ever alive: 29152
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
