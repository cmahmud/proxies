# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 399
- HTTP: 253 alive / 86 gold
- HTTPS: 158 alive / 27 gold
- SOCKS4: 212 alive / 123 gold
- SOCKS5: 257 alive / 163 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32157
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
