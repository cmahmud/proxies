# SyndProxy private pool

## Current pool

- Alive now: 1182
- Gold now: 423
- HTTP: 439 alive / 101 gold
- HTTPS: 301 alive / 33 gold
- SOCKS4: 204 alive / 132 gold
- SOCKS5: 238 alive / 157 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31097
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
