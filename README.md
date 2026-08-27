# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 403
- HTTP: 102 alive / 62 gold
- HTTPS: 172 alive / 17 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41054
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
