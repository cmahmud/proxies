# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 412
- HTTP: 93 alive / 63 gold
- HTTPS: 65 alive / 21 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36897
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
