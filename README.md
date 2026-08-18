# SyndProxy private pool

## Current pool

- Alive now: 1063
- Gold now: 215
- HTTP: 443 alive / 26 gold
- HTTPS: 156 alive / 10 gold
- SOCKS4: 230 alive / 97 gold
- SOCKS5: 234 alive / 82 gold

## Historical pool

- Discovered: 86776
- Ever alive: 7957
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
