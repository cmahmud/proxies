# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 404
- HTTP: 81 alive / 59 gold
- HTTPS: 96 alive / 20 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 173 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42960
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
