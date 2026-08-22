# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 427
- HTTP: 360 alive / 90 gold
- HTTPS: 214 alive / 32 gold
- SOCKS4: 242 alive / 146 gold
- SOCKS5: 272 alive / 159 gold

## Historical pool

- Discovered: 164928
- Ever alive: 32169
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
