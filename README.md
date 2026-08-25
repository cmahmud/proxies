# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 416
- HTTP: 91 alive / 65 gold
- HTTPS: 68 alive / 24 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36941
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
