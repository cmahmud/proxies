# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 541
- HTTP: 376 alive / 164 gold
- HTTPS: 253 alive / 92 gold
- SOCKS4: 207 alive / 145 gold
- SOCKS5: 206 alive / 140 gold

## Historical pool

- Discovered: 123169
- Ever alive: 18810
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
