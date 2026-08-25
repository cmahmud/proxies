# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 406
- HTTP: 79 alive / 59 gold
- HTTPS: 56 alive / 18 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 197 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36700
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
