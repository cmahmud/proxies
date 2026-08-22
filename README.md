# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 395
- HTTP: 323 alive / 87 gold
- HTTPS: 235 alive / 24 gold
- SOCKS4: 237 alive / 137 gold
- SOCKS5: 263 alive / 147 gold

## Historical pool

- Discovered: 164253
- Ever alive: 32110
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
