# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 406
- HTTP: 95 alive / 60 gold
- HTTPS: 60 alive / 21 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41717
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
