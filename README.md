# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 403
- HTTP: 268 alive / 96 gold
- HTTPS: 178 alive / 30 gold
- SOCKS4: 204 alive / 141 gold
- SOCKS5: 239 alive / 136 gold

## Historical pool

- Discovered: 163262
- Ever alive: 31782
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
