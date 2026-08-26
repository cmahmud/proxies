# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 398
- HTTP: 127 alive / 72 gold
- HTTPS: 152 alive / 17 gold
- SOCKS4: 161 alive / 151 gold
- SOCKS5: 184 alive / 158 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40196
- Ever gold: 1307

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
