# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 368
- HTTP: 92 alive / 45 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 180 alive / 154 gold
- SOCKS5: 200 alive / 157 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32958
- Ever gold: 1219

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
