# SyndProxy private pool

## Current pool

- Alive now: 644
- Gold now: 239
- HTTP: 174 alive / 31 gold
- HTTPS: 77 alive / 9 gold
- SOCKS4: 191 alive / 109 gold
- SOCKS5: 202 alive / 90 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7598
- Ever gold: 339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
