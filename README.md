# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 412
- HTTP: 88 alive / 61 gold
- HTTPS: 85 alive / 18 gold
- SOCKS4: 181 alive / 165 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41565
- Ever gold: 1339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
