# SyndProxy private pool

## Current pool

- Alive now: 686
- Gold now: 385
- HTTP: 191 alive / 75 gold
- HTTPS: 105 alive / 18 gold
- SOCKS4: 187 alive / 148 gold
- SOCKS5: 203 alive / 144 gold

## Historical pool

- Discovered: 147187
- Ever alive: 25838
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
