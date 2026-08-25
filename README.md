# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 412
- HTTP: 81 alive / 58 gold
- HTTPS: 66 alive / 18 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 190 alive / 175 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36300
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
