# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 416
- HTTP: 83 alive / 58 gold
- HTTPS: 63 alive / 20 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 190 alive / 175 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36296
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
