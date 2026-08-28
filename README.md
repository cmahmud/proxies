# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 406
- HTTP: 83 alive / 61 gold
- HTTPS: 94 alive / 19 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 176 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42946
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
