# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 406
- HTTP: 99 alive / 64 gold
- HTTPS: 105 alive / 17 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 184 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42664
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
