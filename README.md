# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 507
- HTTP: 376 alive / 171 gold
- HTTPS: 239 alive / 47 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 217 alive / 146 gold

## Historical pool

- Discovered: 124827
- Ever alive: 19164
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
