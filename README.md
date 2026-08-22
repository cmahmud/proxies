# SyndProxy private pool

## Current pool

- Alive now: 923
- Gold now: 411
- HTTP: 278 alive / 88 gold
- HTTPS: 187 alive / 28 gold
- SOCKS4: 216 alive / 143 gold
- SOCKS5: 242 alive / 152 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32160
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
