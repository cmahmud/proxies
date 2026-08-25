# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 414
- HTTP: 88 alive / 57 gold
- HTTPS: 61 alive / 19 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36292
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
