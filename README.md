# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 399
- HTTP: 263 alive / 91 gold
- HTTPS: 156 alive / 21 gold
- SOCKS4: 202 alive / 125 gold
- SOCKS5: 262 alive / 162 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32151
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
