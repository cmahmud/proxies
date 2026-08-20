# SyndProxy private pool

## Current pool

- Alive now: 1430
- Gold now: 546
- HTTP: 551 alive / 178 gold
- HTTPS: 416 alive / 83 gold
- SOCKS4: 222 alive / 130 gold
- SOCKS5: 241 alive / 155 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22986
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
