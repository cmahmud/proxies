# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 418
- HTTP: 93 alive / 59 gold
- HTTPS: 89 alive / 23 gold
- SOCKS4: 176 alive / 167 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41538
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
