# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 402
- HTTP: 118 alive / 74 gold
- HTTPS: 160 alive / 20 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 191 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40180
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
