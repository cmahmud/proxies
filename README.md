# SyndProxy private pool

## Current pool

- Alive now: 1169
- Gold now: 546
- HTTP: 424 alive / 191 gold
- HTTPS: 313 alive / 82 gold
- SOCKS4: 223 alive / 130 gold
- SOCKS5: 209 alive / 143 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19826
- Ever gold: 801

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
