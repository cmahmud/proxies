# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 406
- HTTP: 101 alive / 64 gold
- HTTPS: 164 alive / 16 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41074
- Ever gold: 1317

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
