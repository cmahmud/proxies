# SyndProxy private pool

## Current pool

- Alive now: 853
- Gold now: 405
- HTTP: 221 alive / 94 gold
- HTTPS: 161 alive / 23 gold
- SOCKS4: 209 alive / 134 gold
- SOCKS5: 262 alive / 154 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29028
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
