# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 412
- HTTP: 88 alive / 57 gold
- HTTPS: 64 alive / 18 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36281
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
