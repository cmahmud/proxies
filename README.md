# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 405
- HTTP: 121 alive / 82 gold
- HTTPS: 71 alive / 18 gold
- SOCKS4: 166 alive / 147 gold
- SOCKS5: 183 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48065
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
