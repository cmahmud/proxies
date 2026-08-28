# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 406
- HTTP: 85 alive / 62 gold
- HTTPS: 102 alive / 17 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42945
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
