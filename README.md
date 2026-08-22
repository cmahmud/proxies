# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 415
- HTTP: 357 alive / 89 gold
- HTTPS: 217 alive / 28 gold
- SOCKS4: 227 alive / 144 gold
- SOCKS5: 245 alive / 154 gold

## Historical pool

- Discovered: 164926
- Ever alive: 32162
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
