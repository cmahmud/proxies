# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 412
- HTTP: 81 alive / 58 gold
- HTTPS: 65 alive / 19 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36301
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
