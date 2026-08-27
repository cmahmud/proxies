# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 411
- HTTP: 97 alive / 72 gold
- HTTPS: 104 alive / 19 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42019
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
