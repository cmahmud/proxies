# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 412
- HTTP: 86 alive / 57 gold
- HTTPS: 62 alive / 19 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36285
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
