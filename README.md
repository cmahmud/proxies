# SyndProxy private pool

## Current pool

- Alive now: 1234
- Gold now: 560
- HTTP: 444 alive / 181 gold
- HTTPS: 315 alive / 93 gold
- SOCKS4: 225 alive / 129 gold
- SOCKS5: 250 alive / 157 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22954
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
