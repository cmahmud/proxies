# SyndProxy private pool

## Current pool

- Alive now: 646
- Gold now: 239
- HTTP: 175 alive / 31 gold
- HTTPS: 77 alive / 9 gold
- SOCKS4: 192 alive / 109 gold
- SOCKS5: 202 alive / 90 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7599
- Ever gold: 339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
