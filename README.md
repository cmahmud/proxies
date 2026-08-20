# SyndProxy private pool

## Current pool

- Alive now: 848
- Gold now: 394
- HTTP: 262 alive / 87 gold
- HTTPS: 173 alive / 20 gold
- SOCKS4: 209 alive / 144 gold
- SOCKS5: 204 alive / 143 gold

## Historical pool

- Discovered: 144823
- Ever alive: 25322
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
