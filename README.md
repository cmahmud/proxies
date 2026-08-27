# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 418
- HTTP: 97 alive / 68 gold
- HTTPS: 108 alive / 21 gold
- SOCKS4: 173 alive / 164 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41462
- Ever gold: 1332

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
