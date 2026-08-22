# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 422
- HTTP: 304 alive / 79 gold
- HTTPS: 192 alive / 28 gold
- SOCKS4: 221 alive / 140 gold
- SOCKS5: 268 alive / 175 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32232
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
