# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 443
- HTTP: 295 alive / 97 gold
- HTTPS: 220 alive / 33 gold
- SOCKS4: 212 alive / 147 gold
- SOCKS5: 262 alive / 166 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31055
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
