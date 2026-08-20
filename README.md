# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 390
- HTTP: 164 alive / 71 gold
- HTTPS: 116 alive / 20 gold
- SOCKS4: 193 alive / 143 gold
- SOCKS5: 211 alive / 156 gold

## Historical pool

- Discovered: 145572
- Ever alive: 25528
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
