# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 400
- HTTP: 99 alive / 59 gold
- HTTPS: 60 alive / 21 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41712
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
