# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 393
- HTTP: 173 alive / 76 gold
- HTTPS: 144 alive / 19 gold
- SOCKS4: 207 alive / 143 gold
- SOCKS5: 213 alive / 155 gold

## Historical pool

- Discovered: 145568
- Ever alive: 25515
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
