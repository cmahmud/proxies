# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 411
- HTTP: 103 alive / 64 gold
- HTTPS: 158 alive / 18 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 197 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41099
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
